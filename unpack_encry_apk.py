import argparse
from zipfile import ZipFile, ZipInfo

class ApkFile(ZipFile):
  def extract(self, member, path=None, pwd=None):
		if not isinstance(member, ZipInfo):
			member = self.getinfo(member)
		member.flag_bits ^= member.flag_bits%2
		ZipFile.extract(self, member, path, pwd)
		print 'extracting %s' % member.filename


	def extractall(self, path=None, members=None, pwd=None):
		map(lambda entry: self.extract(entry, path, pwd), members if members is not None  and len(members)>0 else self.filelist)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='unpacks an APK that contains files which are wrongly marked as encrypted')
	parser.add_argument('apk', type=str)
	parser.add_argument('file', type=str, nargs='*')
	args = parser.parse_args()

	apk = ApkFile(args.apk,'r')
	apk.extractall(members=args.file)
