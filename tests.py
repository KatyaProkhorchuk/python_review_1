import os
import shell
import sys
import unittest



class TestBash(unittest.TestCase):

    def test_cd(self):
        test = ['cd', 'aa/gg/hh']
        self.assertEqual(2, shell.def_cd(test))

    def test_dir(self):
        os.mkdir('testdir')
        test = ['rmdir', 'testdir']
        self.assertEqual(1, shell.del_dir(test))
        self.assertEqual(2, shell.del_dir(test))

    def test_make_dir(self):
        # os.mkdir('testdir')
        test = ['rmdir', 'testdir']
        self.assertEqual(1, shell.make_folder(test))
        self.assertEqual(2, shell.make_folder(test))
        os.rmdir('testdir')

    def test_copy(self):
        test = ['cp', 'test.txt', 'test1.txt']

        file = open('test.txt', "a")
        file.write("hello")
        file.close()
        file = open('test1.txt', "a")
        file.write("hello world")
        file.close()
        self.assertEqual(1, shell.copy(test))
        os.remove('test.txt')
        os.remove('test1.txt')
        test = ['cp', 'test.txt']
        self.assertEqual(2, shell.copy(test))
        

    def test_move(self):
        test = ['mv', 'test.txt']
        self.assertEqual(2, shell.move(test))
        os.mkdir('testdir')
        test = ['mv', 'test.txt', 'testdir/']
        self.assertEqual(2, shell.move(test))
        os.rmdir('testdir')

    def test_execute(self):
        self.assertEqual(1, shell.execute('pwd'))

    def test_delete(self):
        file = open('file.txt', 'a')
        file.close()
        test = ['rm', 'test.txt']
        self.assertEqual(2, shell.delete(test))
        test = ['rm', 'file.txt']
        self.assertEqual(1, shell.delete(test))
    def test_cmd_token(self):
        test =['mkdir','test']
        str = "mkdir test"
        self.assertEqual(test, shell.cmd_token(str))
    def test_execute(self):
        test = ['run','ls']
        self.assertEqual(1, shell.execute(test))
        test = ['run','lkjhg','kjhgf']
        self.assertEqual(1, shell.execute(test))
        test = ['ls']
        self.assertEqual(1, shell.execute(test))
        test = ['mkdir','test']
        self.assertEqual(1, shell.execute(test))
        test = ['cd','test']
        self.assertEqual(1, shell.execute(test))
        test = ['run','ls']
        self.assertEqual(1, shell.execute(test))
        test = ['cp','README.md','test']
        self.assertEqual(1, shell.execute(test))
        test = ['rm','test/README.md']
        self.assertEqual(1, shell.execute(test))
        test = ['mv','README.md','test/']
        self.assertEqual(1, shell.execute(test))
        test = ['rmdir','test']
        self.assertEqual(1, shell.execute(test))
        test = ['pwd']
        self.assertEqual(1, shell.execute(test))
        
        self.assertEqual(1, shell.execute(test))
        test = ['exit']
        self.assertEqual(0, shell.execute(test))
    def test_run(self):
        test = ['run','mv','README.md','test/']
        self.assertEqual(1, shell.run(test))


