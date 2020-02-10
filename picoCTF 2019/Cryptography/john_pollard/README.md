# john_pollard

## Question
Sometimes RSA certificates are breakable

## Solution
The given file:
```
-----BEGIN CERTIFICATE-----
MIIB6zCB1AICMDkwDQYJKoZIhvcNAQECBQAwEjEQMA4GA1UEAxMHUGljb0NURjAe
Fw0xOTA3MDgwNzIxMThaFw0xOTA2MjYxNzM0MzhaMGcxEDAOBgNVBAsTB1BpY29D
VEYxEDAOBgNVBAoTB1BpY29DVEYxEDAOBgNVBAcTB1BpY29DVEYxEDAOBgNVBAgT
B1BpY29DVEYxCzAJBgNVBAYTAlVTMRAwDgYDVQQDEwdQaWNvQ1RGMCIwDQYJKoZI
hvcNAQEBBQADEQAwDgIHEaTUUhKxfwIDAQABMA0GCSqGSIb3DQEBAgUAA4IBAQAH
al1hMsGeBb3rd/Oq+7uDguueopOvDC864hrpdGubgtjv/hrIsph7FtxM2B4rkkyA
eIV708y31HIplCLruxFdspqvfGvLsCynkYfsY70i6I/dOA6l4Qq/NdmkPDx7edqO
T/zK4jhnRafebqJucXFH8Ak+G6ASNRWhKfFZJTWj5CoyTMIutLU9lDiTXng3rDU1
BhXg04ei1jvAf0UrtpeOA6jUyeCLaKDFRbrOm35xI79r28yO8ng1UAzTRclvkORt
b8LMxw7e+vdIntBGqf7T25PLn/MycGPPvNXyIsTzvvY/MXXJHnAqpI5DlqwzbRHz
q16/S1WLvzg4PsElmv1f
-----END CERTIFICATE-----
```

After decrypting it, it gives us:
```
[
    [
        Version: V1
        Subject: CN=PicoCTF, C=US, ST=PicoCTF, L=PicoCTF, O=PicoCTF, OU=PicoCTF
        Signature Algorithm: MD2withRSA, OID = 1.2.840.113549.1.1.2

        Key:  RSA Public Key [68:0d:58:fa:65:c4:fc:08:fa:45:55:37:9d:3d:e0:19:ec:29:d6:6c]
                    modulus: 11a4d45212b17f
            public exponent: 10001

        Validity: [From: Mon Jul 08 07:21:18 UTC 2019,
                    To: Wed Jun 26 17:34:38 UTC 2019]
        Issuer: CN=PicoCTF
        SerialNumber: [    3039]
    ]
    Algorithm: [MD2withRSA]
    Signature:
    0000: 07 6A 5D 61 32 C1 9E 05   BD EB 77 F3 AA FB BB 83  .j]a2.....w.....
    0010: 82 EB 9E A2 93 AF 0C 2F   3A E2 1A E9 74 6B 9B 82  ......./:...tk..
    0020: D8 EF FE 1A C8 B2 98 7B   16 DC 4C D8 1E 2B 92 4C  ..........L..+.L
    0030: 80 78 85 7B D3 CC B7 D4   72 29 94 22 EB BB 11 5D  .x......r)."...]
    0040: B2 9A AF 7C 6B CB B0 2C   A7 91 87 EC 63 BD 22 E8  ....k..,....c.".
    0050: 8F DD 38 0E A5 E1 0A BF   35 D9 A4 3C 3C 7B 79 DA  ..8.....5..<<.y.
    0060: 8E 4F FC CA E2 38 67 45   A7 DE 6E A2 6E 71 71 47  .O...8gE..n.nqqG
    0070: F0 09 3E 1B A0 12 35 15   A1 29 F1 59 25 35 A3 E4  ..>...5..).Y%5..
    0080: 2A 32 4C C2 2E B4 B5 3D   94 38 93 5E 78 37 AC 35  *2L....=.8.^x7.5
    0090: 35 06 15 E0 D3 87 A2 D6   3B C0 7F 45 2B B6 97 8E  5.......;..E+...
    00A0: 03 A8 D4 C9 E0 8B 68 A0   C5 45 BA CE 9B 7E 71 23  ......h..E....q#
    00B0: BF 6B DB CC 8E F2 78 35   50 0C D3 45 C9 6F 90 E4  .k....x5P..E.o..
    00C0: 6D 6F C2 CC C7 0E DE FA   F7 48 9E D0 46 A9 FE D3  mo.......H..F...
    00D0: DB 93 CB 9F F3 32 70 63   CF BC D5 F2 22 C4 F3 BE  .....2pc...."...
    00E0: F6 3F 31 75 C9 1E 70 2A   A4 8E 43 96 AC 33 6D 11  .?1u..p*..C..3m.
    00F0: F3 AB 5E BF 4B 55 8B BF   38 38 3E C1 25 9A FD 5F  ..^.KU..88>.%.._
]
```

The question hinted us to search for "John Pollard" and the we need to factorize the modulus. Try to find the factorization using Pollard's Algorithm:
```python
# Extended Euclidean Algorithm to find greatest common divisor
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

def pollardRho(n):
    x = 2
    y = 2
    d = 1
    f = lambda x: (x ** 2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d, _, _ = egcd(abs(x - y), n)
    if d != n:
        return d

b = int("11a4d45212b17f", 16)
print(pollardRho(b))
print(b // pollardRho(b))
```

flag: `picoCTF{73176001,67867967}`