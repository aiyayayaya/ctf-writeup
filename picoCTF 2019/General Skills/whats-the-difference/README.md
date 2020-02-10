# whats-the-difference

## Question
Can you spot the difference? kitters cattos. They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server

## Solution
As the hints told us to find the difference of the two pictures, lets try to do it.

```python
kitters = open('kitters.jpg', 'rb').read()
cattos = open('cattos.jpg', 'rb').read()
diff = [(kitters[i], cattos[i]) for i in range(len(kitters)) if kitters[i] != cattos[i]]
print(diff)
```

Our results:
```
[(153, 112), (157, 105), (152, 99), (200, 111), (10, 67), (244, 84), (107, 70), (177, 123), (152, 116), (146, 104), (13, 51), (216, 121), (82, 114), (124, 51), (249, 95), (142, 97), (245, 53), (230, 95), (240, 100), (74, 49), (170, 102), (225, 102), (200, 51), (63, 114), (71, 51), (19, 110), (163, 116), (49, 95), (75, 52), (188, 115), (196, 95), (35, 98), (174, 117), (6, 55), (206, 55), (230, 51), (231, 114), (138, 95), (82, 52), (254, 110), (35, 100), (255, 95), (156, 106), (228, 51), (131, 49), (146, 49), (114, 121), (5, 95), (123, 97), (7, 115), (192, 108), (43, 107), (103, 106), (238, 102), (41, 100), (148, 115), (128, 97), (70, 108), (143, 107), (110, 102), (4, 115), (229, 108), (224, 107), (5, 102), (159, 108), (210, 107), (64, 106), (34, 100), (144, 115), (133, 102), (205, 100), (164, 115), (141, 122), (103, 109), (175, 122), (126, 49), (225, 48), (239, 53), (136, 52), (25, 56), (11, 125)]
```

The ASCII code for 'p' is 112, so we guessed that cattos has a hidden flag in it. Lets try to decode it:
```python
print(''.join([chr(i[1]) for i in diff]))
```

This gives us the flag!

Flag: `picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}`