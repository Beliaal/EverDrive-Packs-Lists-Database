#!/usr/bin/python3
from os.path import exists
import argparse
import datetime

AUTHOR = 'nedala'
HOMEPAGE = 'A Winrar is you!'
URL = 'https://www.winrar.com'


def create_db(_output):
	frw = open(_output, "w")
	frw.close()


def writeftr(_input):
	frw = open(_input, "a")
	frw.write("</datafile>")
	frw.close()


def writehdr(_input):
	header = ['<?xml version="1.0"?>']
	header.append('<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">')
	header.append('<datafile>')
	header.append('\t<header>')
	header.append('\t\t<name>HTGDB database conversion</name>')
	header.append('\t\t<description>Converted from HTGDB to Logiqx</description>')
	header.append('\t\t<version>{0}</version>'.format(datetime.datetime.now().strftime("%Y%m%d-%H%M")))
	header.append('\t\t<author>{0}</author>'.format(AUTHOR))
	header.append('\t\t<homepage>{0}</homepage>'.format(HOMEPAGE))
	header.append('\t\t<url>{0}</url>'.format(URL))
	header.append('\t</header>')
	frw = open(_input, "a")
	for _val in header:
		frw.write(_val + "\n")
	frw.close()


def writelns(towrite, _input):
	frw = open(_input, "a")
	for _val in towrite:
		frw.write(_val + "\n")
	frw.close()


def readlns(_input, _output):
	dataset = dict()
	dic_rot = 0  # How many rotations have we spun the dict...

	frw = open(_input, "r")
	for _line in frw:
		_line = _line.replace('&', '&amp;')  # XML needs &amp;, not &...
		# If any spaces exists where we expect <TAB>, fix them...
		_line = _line.replace('    ', '\t')
		temp = _line.rstrip().split("\t")  # Split on <TAB>

		_sha256 = temp[0]  # sha256 | Not in use...
		_sha1 = temp[2]  # sha1
		_md5 = temp[3]  # md5
		_crc32 = temp[4]  # crc32
		_fsize = temp[5]  # File Size
		_fpath = temp[1].split("/", 1)[1]  # Filepath in database
		_rname = _fpath.rsplit("/", 1)[1].split(".")[0]  # ROM name
		_dbnme = temp[1].split("/", 1)[0]  # Database Name

#	temp = temp[-1].rsplit("/", 1)

		_gname = _rname.rsplit(".", 1)
		_gname = _gname[0]  # Game's name

		if dic_rot == 0:
			writehdr(_output)

		# Construct a game dictionary/container in Logiqx format...
		temp = ['\t<game name=\"{0}\">'.format(_gname)]
		temp.append('\t\t<comment>Part of DB: \"{0}\" | Filepath: \"{1}\"</comment>'.format(_dbnme, _fpath))
		temp.append('\t\t<description>{0}</description>'.format(_gname))
		temp.append('\t\t<rom name=\"{0}\" size=\"{1}\" crc=\"{2}\" md5=\"{3}\" sha1=\"{4}\"/>'.format(_fpath, _fsize, _crc32, _md5, _sha1))
		temp.append('\t</game>')

		dataset.update({dic_rot: {"dat": temp}})
		dic_rot += 1

	frw.close()
	return dataset


def main():
	parser = argparse.ArgumentParser(prog='htgd2dat', description='Convert htgd databases to logicqX XML datfiles for use in standard rom managers...')
	parser.add_argument('-i', '--input', help='The filename of the databaste that is to be converted', required=True)
	parser.add_argument('-o', '--output', nargs='?', help='The name of the converted file...', required=True)
	args = parser.parse_args()

	create_db(args.output)

	file_exists = exists(args.input)
	if file_exists:
		datdb = readlns(str(args.input), args.output)
		for gid in datdb.values():
			writelns(gid.get("dat"), args.output)
			writeftr(args.output)
	else:
		print('Input file does not exist... [{0}]'.format(args.input))


if __name__ == "__main__":
	main()
