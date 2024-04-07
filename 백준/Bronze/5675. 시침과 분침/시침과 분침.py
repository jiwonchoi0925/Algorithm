import sys

h_ang = -6
m_ang = -6
angs = set()
for hour in range(24):
    for minute in range(60):
        m_ang = (m_ang + 6) % 360
        if m_ang % 72 == 0:
            h_ang = (h_ang + 6) % 360
        b_ang = (h_ang - m_ang) % 360
        the_other = 360 - b_ang
        angs.add(min(b_ang, the_other))
angs = list(angs)
for i in sys.stdin.readlines():
    if int(i.strip()) in angs:
        print("Y")
    else:
        print("N")