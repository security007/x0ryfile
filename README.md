# x0ryfile
File data encryption with Xor algorithm (Protect your file privacy with this tool)

## Usage
```Bash
usage: x0r.py [-h] -F FILE [-E] [-D] [-K KEY] -O OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -F FILE, --file FILE  File to encrypt/decrypt
  -E, --encrypt         Encrypt file
  -D, --decrypt         Decrypt file (required key argument)
  -K KEY, --key KEY     Key to decrypt file
  -O OUTPUT, --output OUTPUT
                        Output file

```
## Encrypt

```bash
python3 x0r.py -F myfile.txt -E -O encrypted
```
## Decrypt

```bash
python3 x0r.py -F myfile.x0r -D -K myrandomkey -O decrypt.txt
```
