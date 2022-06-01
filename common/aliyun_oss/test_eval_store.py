from common.aliyun_oss import bucket

class TestEvalStore():
    prefix = ''

    @staticmethod
    def put_file(key, file_path):
        return bucket.put_object_from_file(TestEvalStore.prefix+key, file_path)

    @staticmethod
    def is_exist(key):
        return bucket.object_exists(TestEvalStore.prefix+key)

    @staticmethod
    def get(key, file_path):
        return bucket.get_object_to_file(TestEvalStore.prefix+key, file_path)