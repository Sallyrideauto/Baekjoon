price = []

sd = int(input())
jd = int(input())
hd = int(input())
coke = int(input())
spr = int(input())

sd_coke = sd + coke - 50
price.append(sd_coke)
sd_spr = sd + spr - 50
price.append(sd_spr)
jd_coke = jd + coke - 50
price.append(jd_coke)
jd_spr = jd + spr - 50
price.append(jd_spr)
hd_coke = hd + coke - 50
price.append(hd_coke)
hd_spr = hd + spr - 50
price.append(hd_spr)

print(min(price))