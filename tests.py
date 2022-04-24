from shell import *
import unittest



class TestBash(unittest.TestCase):

    def test_cd(self):
        test = ['cd', 'aa/gg/hh']
        self.assertEqual(2, def_cd(test))

    def test_dir(self):
        os.mkdir('testdir')
        test = ['rmdir', 'testdir']
        self.assertEqual(1, del_dir(test))
        self.assertEqual(2, del_dir(test))

    def test_make_dir(self):
        # os.mkdir('testdir')
        test = ['rmdir', 'testdir']
        self.assertEqual(1, make_folder(test))
        self.assertEqual(2, make_folder(test))
        os.rmdir('testdir')

    def test_copy(self):
        test = ['cp', 'test.txt', 'test1.txt']

        file = open('test.txt', "a")
        file.write("hello")
        file.close()
        file = open('test1.txt', "a")
        file.write("hello world")
        file.close()
        self.assertEqual(1, copy(test))
        os.remove('test.txt')
        os.remove('test1.txt')
        test = ['cp', 'test.txt']
        self.assertEqual(2, copy(test))

    def test_move(self):
        test = ['mv', 'test.txt']
        self.assertEqual(2, move(test))
        os.mkdir('testdir')
        test = ['mv', 'test.txt', 'testdir/']
        self.assertEqual(2, move(test))
        os.rmdir('testdir')

    def test_execute(self):
        self.assertEqual(1, execute('pwd'))

    def test_delete(self):
        file = open('file.txt', 'a')
        file.close()
        test = ['rm', 'test.txt']
        self.assertEqual(2, delete(test))
        test = ['rm', 'file.txt']
        self.assertEqual(1, delete(test))
