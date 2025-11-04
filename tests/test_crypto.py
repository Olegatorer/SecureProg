import os

from crypto import generate_key, encrypt_file, decrypt_file


def test_encryption_decryption(tmp_path):
    generate_key()
    test_file = tmp_path / "test.txt"
    test_file.write_text("Secret Data")

    encrypt_file(str(test_file))
    encrypted_file = str(test_file) + ".enc"
    assert os.path.exists(encrypted_file)

    decrypt_file(encrypted_file)
    decrypted_file = str(test_file) + ".dec"
    assert os.path.exists(decrypted_file)
    assert open(decrypted_file).read() == "Secret Data"