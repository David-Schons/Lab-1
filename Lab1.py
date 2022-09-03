human_age = float(input("Enter your age:   "))
#In order to convert a float of years, I created seperate variables for a rounded down integer, and the original float
#by subtracting the int from the float, Im able to use the remainder to convert to months, then repeat to get days
dog_age = 7
human_in_dog_years = human_age * dog_age
human_in_dog_years_display = int((human_in_dog_years))
human_in_dog_months = human_in_dog_years - human_in_dog_years_display
human_in_dog_months_display=int((human_in_dog_months*12))
human_in_dog_days = (human_in_dog_months * 12) - human_in_dog_months_display
human_in_dog_days_display = int((human_in_dog_days*30))
print("your age in dog years is",human_in_dog_years_display,"years",human_in_dog_months_display,"months",human_in_dog_days_display,"days")

cat_age = 9

human_in_cat_years = human_age / cat_age
human_in_cat_years_display = int((human_in_cat_years))
human_in_cat_months = human_in_cat_years - human_in_cat_years_display
human_in_cat_months_display = int((human_in_cat_months * 12))
human_in_cat_days = (human_in_cat_months * 12) - human_in_cat_months_display
human_in_cat_days_display =  int((human_in_cat_days * 30))
print("your age in cat years is",human_in_cat_years_display,"years",human_in_cat_months_display,"months",human_in_cat_days_display,"days")

human_in_horse_years = 3*((((human_age**2)-47)/7)+12)
human_in_horse_years_display = int(human_in_horse_years)
human_in_horse_months = human_in_horse_years - human_in_horse_years_display
human_in_horse_months_display = int((human_in_horse_months * 12))
human_in_horse_days = (human_in_horse_months * 12) - human_in_horse_months_display
human_in_horse_days_display = int((human_in_horse_days * 30))
print("your age in horse years is",human_in_horse_years_display,"years",human_in_horse_months_display,"months",human_in_horse_days_display,"days")
