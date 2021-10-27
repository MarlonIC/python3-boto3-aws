import json

request_ids = [
    55235, 55234, 55233, 55232, 55231, 55230, 55229, 55228, 55227, 55226, 55225, 55224, 55223, 55222, 55221, 55220,
    55219, 55218, 55217, 55216, 55215, 55214, 55213, 55212, 55211, 55210, 55209, 55208, 55207, 55206, 55205, 55204,
    55203, 55202, 55201, 55200, 55199, 55198, 55197, 55196, 55195, 55194, 55193, 55192, 55191, 55190, 55189, 55188,
    55187, 55186, 55185, 55184, 55183, 55182, 55181, 55180, 55179, 55178, 55177, 55176, 55175, 55174, 55173, 55172,
    55171, 55170, 55169, 55168, 55167, 55166, 55165, 55164, 55163, 55162, 55161, 55160, 55159, 55158, 55157, 55156,
    55155, 55154, 55153, 55152, 55151, 55150, 55149, 55148, 55147, 55146, 55145, 55144, 55143, 55142, 55141, 55140,
    55139, 55138, 55137, 55136, 55135, 55134, 55133, 55132, 55131, 55130, 55129, 55128, 55127, 55126, 55125, 55124,
    55123, 55122, 55121, 55120, 55119, 55118, 55117, 55116, 55115, 55114, 55113, 55112, 55111, 55110, 55109, 55108,
    55107, 55106, 55105, 55104, 55103, 55102, 55101, 55100, 55099, 55098, 55097, 55096, 55095, 55094, 55093, 55092,
    55091, 55090, 55089, 55088, 55087, 55086, 55085, 55084, 55083, 55082, 55081, 55080, 55079, 55078, 55077, 55022,
    54920, 54851, 54849, 54847, 54821, 54787, 54785, 54782, 54780, 54764
]

sample = {
    'requestId': '',
    'ttl': 1638910054,
    'messageId': '33113404796703574316',
    'status': 'DELIVERED_TO_HANDSET'
}
data = []

for request_id in request_ids:
    sample['requestId'] = str(request_id)
    data.append(sample.copy())

json_object = json.dumps(data, indent=4)
with open('result.json', 'w') as outfile:
    outfile.write(json_object)
