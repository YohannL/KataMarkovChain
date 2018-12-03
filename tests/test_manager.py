from KataMarkovChain.Core.Manager import Manager

SPLIT_PATH = "KataMarkovChain.Core.TextSplitter.TextSplitter.split"


class TestManager:

    @staticmethod
    def test_create_new_mv():
        manager = Manager()
        new_mv = manager.create_new_mv("test")
        assert new_mv is not None
        assert new_mv.word == "test"

    @staticmethod
    def test_create_unique_new_mv():
        manager = Manager()
        new_mv_1 = manager.create_new_mv("test")
        new_mv_2 = manager.create_new_mv("test")
        assert new_mv_1 is not None
        assert new_mv_1.word == "test"
        assert new_mv_2 is not None
        assert new_mv_2.word == "test"
        assert new_mv_1 is new_mv_2

    @staticmethod
    def test_manager_run():
        manager = Manager()
        manager.run("This is a test.")
        assert True
