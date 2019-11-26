#! /usr/bin/env python
#-*- coding: utf-8 -*-

import json
import tarfile
from io import BytesIO
from sqlalchemy import and_
from web.models import JsonObject

def check_duplicates(json_object):
    """Check for duplicates, by UUID, of the object given in parameter.
    """
    duplicates = []
    # extract the JSON part of the JsonObject
    json_obj = json_object.json_object
    if isinstance(json_obj, list):
        # if we have a list of JSON objects with a UUI for each of them
        for elem in json_obj:
            if elem.get('uuid', False):
                duplicate = JsonObject.query.filter(and_(
                    JsonObject.json_object[('uuid')].astext == elem['uuid']),
                    JsonObject.id != json_object.id)
                if duplicate.count() > 0:
                    duplicates.append(duplicate[0])

    if isinstance(json_obj, dict):
        # if we directly have an object
        if json_obj.get('uuid', False):
            duplicate = JsonObject.query.filter(and_(
                JsonObject.json_object[('uuid')].astext == json_obj['uuid']),
                JsonObject.id != json_object.id)
            if duplicate.count() > 0:
                duplicates.append(duplicate[0])

    return duplicates


def generate_misp_galaxy_cluster(json_object):
    """Generates a MISP galaxy and a cluster from an object.
    """
    # Creation of the galaxy
    galaxy = {
        "description": json_object.description,
        "name": json_object.name,
        "type": json_object.schema.name,
        "uuid": json_object.json_object.get('uuid', ''),
        "version": json_object.json_object.get('version', '')
    }
    # Creation of the cluster
    cluster = {
        "uuid": json_object.json_object.get('uuid', ''),
        "name": json_object.name,
        "description": json_object.description,
        "version": json_object.json_object.get('version', ''),
        "type": json_object.schema.name,
        "authors": json_object.json_object.get('authors', ''),
        #"source": "",
        #"category": "",
        "values": []
    }
    for value in json_object.json_object.get('measures', []):
        cluster["values"].append({
            "uuid": value["uuid"],
            "value": value["code"],
            "description": value["label"],
            "meta": {},

        })
    return (galaxy, cluster)


def generate_tar_gz_archive(galaxy, cluster):
    """Generate a tar.gz archive from a MISP galaxy.
    """
    out = BytesIO()
    tar = tarfile.open(mode="w:gz", fileobj=out)

    galaxy_str = json.dumps(galaxy)
    cluster_str = json.dumps(cluster)

    # t = tarfile.TarInfo("galaxy")
    # t.type = tarfile.DIRTYPE
    # tar.addfile(t)

    tarinfo = tarfile.TarInfo('galaxy.json')
    tarinfo.size = len(galaxy_str)
    tar.addfile(tarinfo, BytesIO(galaxy_str.encode()))

    tarinfo = tarfile.TarInfo('cluster.json')
    tarinfo.size = len(cluster_str)
    tar.addfile(tarinfo, BytesIO(cluster_str.encode()))

    tar.close()

    return out.getvalue()