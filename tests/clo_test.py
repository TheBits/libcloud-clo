import functools
import os
from pathlib import Path

import pytest
import vcr
from libcloud.common.types import InvalidCredsError

from libcloudcloru import CloDriver


@pytest.fixture()
def credentials() -> str:
    token = os.getenv("DRIVER_TOKEN")
    if token is None:
        pytest.exit("set up DRIVER_TOKEN environment variable")

    return str(token)


def filter_response(response):
    try:
        del response["headers"]["Set-Cookie"]
    except KeyError:
        pass
    return response


def vcr_record(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        path = Path("./tests/fixtures/") / f"{f.__name__}.yaml"
        kwargs = dict(
            filter_headers=["Authorization"],
            decode_compressed_response=True,
            match_on=["method", "path"],
            path=str(path),
        )
        if not path.exists():
            kwargs["before_record_response"] = filter_response
        with vcr.use_cassette(**kwargs):
            return f(*args, **kwds)

    return wrapper


@vcr_record
def test_logon_invalid_creds():
    clo = CloDriver(key="123")
    with pytest.raises(InvalidCredsError):
        clo.list_key_pairs()


@vcr_record
def test_compute_list_locations(credentials):
    clo = CloDriver(credentials)
    locations = clo.list_locations()
    assert locations


@vcr_record
def test_compute_list_key_pairs_empty(credentials):
    clo = CloDriver(key=credentials)
    kps = clo.list_key_pairs()
    assert not kps
