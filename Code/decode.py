from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def AES_decode():
    def aes_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        try:
            decrypted_data = cipher.decrypt(ciphertext)
            # 尝试去除填充
            plaintext = unpad(decrypted_data, AES.block_size)
            return plaintext
        except ValueError as e:
            raise ValueError(f"解密失败: {e}")

    # 示例 AES 解密使用
    # 请根据需要调整密钥和 IV（初始化向量）
    aes_key = b'0123456789abcdef'  # 16 字节的 AES 密钥
    aes_iv = b'abcdef9876543210'  # 16 字节的 IV
    aes_encrypted_data = bytes.fromhex(
        '0B0386263E010047A5EEE500F67AB300A7942F29A787610D00000B2F302D02141C9BD14FC1EFACD709B90FF3B7EB7C23F912A4F7021500B7A4CF3869353AC9EBC788811960FFA559A5DA01000000000000000000000000000000000000000000000000000000000000'
    )

    try:
        aes_decrypted = aes_decrypt(aes_encrypted_data, aes_key, aes_iv)
        print("AES 解密结果:", aes_decrypted)
    except ValueError as e:
        print(f"AES 解密失败: {e}")


def XOR_decode():
    def xor_decrypt(data: bytes, key: bytes) -> bytes:
        return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

    # 示例 XOR 解密使用
    xor_key = b'secretkey'  # 你可以根据实际情况替换密钥
    xor_encrypted_data = bytes.fromhex(
        '0B0386263E010047A5EEE500F67AB300A7942F81A787610D00000B2F302D02144BB86C6ACA48AC43DF5E33E67C0A9FA85E73B5A00215008AFA4861CB0EBECE3D22FC4DE69E387D7777A3B3')

    xor_decrypted = xor_decrypt(xor_encrypted_data, xor_key)
    print("XOR 解密结果:", xor_decrypted)


def DES_decode():
    from Crypto.Cipher import DES
    from Crypto.Util.Padding import unpad

    def des_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
        cipher = DES.new(key, DES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
        return plaintext

    # 示例 DES 解密使用
    # 请根据需要调整密钥和 IV
    des_key = b'12345678'  # 8 字节的 DES 密钥
    des_iv = b'87654321'  # 8 字节的 IV
    des_encrypted_data = bytes.fromhex(
        '0B0386263E010047A5EEE500F67AB300A7942F81A787610D00000B2F302D02144BB86C6ACA48AC43DF5E33E67C0A9FA85E73B5A00215008AFA4861CB0EBECE3D22FC4DE69E387D7777A3B3')

    try:
        des_decrypted = des_decrypt(des_encrypted_data, des_key, des_iv)
        print("DES 解密结果:", des_decrypted)
    except ValueError as e:
        print(f"DES 解密失败: {e}")


if __name__ == '__main__':
    # AES_decode()
    # XOR_decode()
    DES_decode()
