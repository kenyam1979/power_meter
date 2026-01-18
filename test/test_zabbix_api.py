import pytest


def test_call_zabbix_api(monkeypatch):
    class MockResponse:
        def json(self):
            return {
                "jsonrpc": "2.0",
                "result": {"response": "success", "data": [{"itemid": 69141}]},
                "id": 1,
            }

    def mock_post(url, headers, data):
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    from power_meter.lib.zabbix_api import call_zabbix_api

    item_id = "69140"
    value = 123.45

    response = call_zabbix_api(item_id, value)
    assert response["result"]["response"] == "success"
    assert response["result"]["data"][0]["itemid"] == 69141


def test_log_dump(tmp_path):
    response = {
        "jsonrpc": "2.0",
        "result": {"response": "success", "data": [{"itemid": 69141}]},
        "id": 1,
    }

    file_path = tmp_path / "test_log.txt"

    import json
    from power_meter.lib.zabbix_api import log_dump

    log_dump(response, file_path)

    assert file_path.exists()
    assert file_path.read_text() == json.dumps(response) + "\n"
