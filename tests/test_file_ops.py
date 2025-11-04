from file_ops import secure_delete

def test_secure_delete(tmp_path):
    test_file = tmp_path / "delete_me.txt"
    test_file.write_text("Sensitive")
    assert test_file.exists()

    secure_delete(str(test_file))
    assert not test_file.exists()