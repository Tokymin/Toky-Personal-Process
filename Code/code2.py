import zlib


def crc32_full(uid: bytes, data: bytes) -> str:
    """
    计算 UID 和 Data 的全部 CRC 校验值。

    :param uid: UID 二进制数据
    :param data: Data 二进制数据
    :return: 计算后的 CRC32 校验值 (十六进制格式)
    """
    full_data = uid + data
    crc_value = zlib.crc32(full_data)
    return f"{crc_value:08X}"  # 返回十六进制格式


def crc32_with_uid_as_param(uid: bytes, data: bytes) -> str:
    """
    使用 UID 的 CRC 结果作为 Data CRC 校验的参数（偏移值）。

    :param uid: UID 二进制数据
    :param data: Data 二进制数据
    :return: 使用 UID CRC 值作为偏移量后的 Data CRC32 校验值 (十六进制格式)
    """
    # 计算 UID 的 CRC 值
    uid_crc_value = zlib.crc32(uid)

    # 使用 UID 的 CRC 值作为偏移量来计算 Data 的 CRC
    data_crc_value = zlib.crc32(data, uid_crc_value)
    return f"{data_crc_value:08X}"  # 返回十六进制格式


# 第二组数据:
uid_hex = "E00780DDB86E0F4F00"  # 调整字节顺序，高字节在前
data_hex = ("0B0386263E010047A5EEE500F67AB300A7942F81A787610D00000B2F302D02144BB86C"
            "6ACA48AC43DF5E33E67C0A9FA85E73B5A00215008AFA4861CB0EBECE3D22FC4DE69E38"
            "7D7777A3B30000000000000000000000000000000000000000000000000000000000")

# 将 UID 和 Data 转换为二进制格式
uid_bytes = bytes.fromhex(uid_hex)
data_bytes = bytes.fromhex(data_hex)

# 调用第一个函数：计算 UID + Data 的 CRC 校验值
full_crc = crc32_full(uid_bytes, data_bytes)
print(f"UID + Data 的全部 CRC 校验值: {full_crc}")

# 调用第二个函数：使用 UID CRC 结果作为偏移量来计算 Data 的 CRC
param_crc = crc32_with_uid_as_param(uid_bytes, data_bytes)
print(f"使用 UID CRC 值作为参数的 Data CRC 校验值: {param_crc}")
