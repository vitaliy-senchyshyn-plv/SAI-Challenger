import pytest
from sai import SaiObjType

TEST_VLAN_ID = "100"


@pytest.fixture
def sai_virtual_router_obj(npu):
    vrf_oid = npu.create(SaiObjType.VIRTUAL_ROUTER, [])
    yield vrf_oid
    npu.remove(vrf_oid)


virtual_router_attrs = [
    ('SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE',                     "bool",                "true"),
    ('SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE',                     "bool",                "true"),
    ('SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS',                    "sai_mac_t",           "SAI_SWITCH_ATTR_SRC_MAC_ADDRESS"),
    ('SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_TTL1_PACKET_ACTION',       "sai_packet_action_t", "SAI_PACKET_ACTION_TRAP"),
    ('SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_IP_OPTIONS_PACKET_ACTION', "sai_packet_action_t", "SAI_PACKET_ACTION_TRAP"),
    ('SAI_VIRTUAL_ROUTER_ATTR_UNKNOWN_L3_MULTICAST_PACKET_ACTION', "sai_packet_action_t", "SAI_PACKET_ACTION_DROP"),
    ('SAI_VIRTUAL_ROUTER_ATTR_LABEL',                              "char",                ""),
]


@pytest.mark.parametrize(
    "attr,attr_type,attr_val",
    virtual_router_attrs
)
def test_get_before_set_attr(npu, dataplane, sai_virtual_router_obj, attr, attr_type, attr_val):
    status, data = npu.get_by_type(sai_virtual_router_obj, attr, attr_type, do_assert=False)
    npu.assert_status_success(status)
    assert data.value() == attr_val


@pytest.mark.parametrize(
    "attr,attr_value",
    [
        ("SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE",                     "false"),
        ("SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE",                     "true"),
        ("SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE",                     "false"),
        ("SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE",                     "true"),
        ('SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS',                    "SAI_SWITCH_ATTR_SRC_MAC_ADDRESS"),
        ('SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_TTL1_PACKET_ACTION',       "SAI_PACKET_ACTION_TRAP"),
        ('SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_IP_OPTIONS_PACKET_ACTION', "SAI_PACKET_ACTION_TRAP"),
        ('SAI_VIRTUAL_ROUTER_ATTR_UNKNOWN_L3_MULTICAST_PACKET_ACTION', "SAI_PACKET_ACTION_DROP"),
        ('SAI_VIRTUAL_ROUTER_ATTR_LABEL',                              ""),
    ]
)
def test_set_attr(npu, dataplane, sai_virtual_router_obj, attr, attr_value):
    status = npu.set(sai_virtual_router_obj, [attr, attr_value], False)
    npu.assert_status_success(status)


@pytest.mark.parametrize(
    "attr, attr_type, attr_value",
    [
        ("SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE",                     "bool",                "false"),
        ("SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE",                     "bool",                "true"),
        ("SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE",                     "bool",                "false"),
        ("SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE",                     "bool",                "true"),
        ('SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS',                    "sai_mac_t",           "SAI_SWITCH_ATTR_SRC_MAC_ADDRESS"),
        ('SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_TTL1_PACKET_ACTION',       "sai_packet_action_t", "SAI_PACKET_ACTION_TRAP"),
        ('SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_IP_OPTIONS_PACKET_ACTION', "sai_packet_action_t", "SAI_PACKET_ACTION_TRAP"),
        ('SAI_VIRTUAL_ROUTER_ATTR_UNKNOWN_L3_MULTICAST_PACKET_ACTION', "sai_packet_action_t", "SAI_PACKET_ACTION_DROP"),
        ('SAI_VIRTUAL_ROUTER_ATTR_LABEL',                              "char",                ""),
    ]
)
def test_get_after_set_attr(npu, dataplane, sai_virtual_router_obj, attr, attr_type, attr_value):
    npu.set(sai_virtual_router_obj, [attr, attr_value], False)
    status, data = npu.get_by_type(sai_virtual_router_obj, attr, attr_type, do_assert=False)
    npu.assert_status_success(status)
    assert data.value() == attr_value
