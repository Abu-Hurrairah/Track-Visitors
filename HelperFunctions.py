import json
import os
import re
import pyodbc
from flask import jsonify

def load_records(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_records(records, filename):
    with open(filename, 'w') as file:
        json.dump(records, file)


def find_all_paths_recursive(cost_table, start, destinations, path=[]):
    path = path + [start]
    if start in destinations:
        return [path]
    if start not in cost_table:
        return []
    paths = []
    for index, cost in enumerate(cost_table[start]):
        if cost == -1:
            continue
        if 'C{}'.format(index+1) not in path:
            newpaths = find_all_paths_recursive(cost_table, 'C{}'.format(index+1), destinations, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_all_paths(cost_table, source, destinations):
    all_paths = []
    for destination in destinations:
        paths = find_all_paths_recursive(cost_table, source, [destination])
        all_paths.extend(paths)
    return all_paths


def get_image_list(visitor_id):
    image_list = os.listdir(f'Images/{visitor_id}')
    image_list.sort(key=lambda x: int(re.sub('\D', '', x)))
    return jsonify(images=image_list)


def is_visitor_on_correct_path(VisitorPathHistory, CorrectedPaths):
    def is_corrected_path(corrected_path, visitor_history):
        if len(corrected_path) < 2:
            return False

        corrected_length = len(corrected_path)
        visitor_length = len(visitor_history)

        for i in range(corrected_length - visitor_length + 1):
            if visitor_history == corrected_path[i:i + visitor_length]:
                return True

        return False

    path_matched = False
    for path in CorrectedPaths:
        if is_corrected_path(path, VisitorPathHistory):
            path_matched = True
            break

    return path_matched



def get_cost_matrix(conn_string):
    connection = pyodbc.connect(conn_string)
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM Camera")
    camera_names = [row[0] for row in cursor.fetchall()]

    camera_dict = {name: [-1] * len(camera_names) for name in camera_names}

    for source_idx, source_camera in enumerate(camera_names):
        for destination_idx, destination_camera in enumerate(camera_names):
            query = f"SELECT timeToReach FROM Connection WHERE sourceCam_id = (SELECT id FROM Camera WHERE name = '{source_camera}') AND destinationCam_id = (SELECT id FROM Camera WHERE name = '{destination_camera}')"
            cursor.execute(query)
            time_row = cursor.fetchone()
            if time_row:
                time_to_reach = time_row[0]
                camera_dict[source_camera][destination_idx] = time_to_reach

    connection.close()

    costMatrix = {name: times for name, times in zip(camera_names, camera_dict.values())}
    return costMatrix