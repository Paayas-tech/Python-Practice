tool = "Python"
purpose = "Data Analysis"
hours = 10

# 1. Plus (+) Operator (manual spacing required)
concat_str = tool + " is great for " + purpose + "!"
print(concat_str)

# 2. Modern f-strings (standard practice)
f_str = f"Learning {tool} for {purpose} after {hours * 2} hours of practice."
print(f_str)

# 3. Alternative formatting: str.format()
format_str = "Study: {} | Goal: {}".format(tool, purpose)
print(format_str)

# 4. Alternative formatting: %-formatting (legacy)
percent_str = "Language: %s | Hours: %d" % (tool, hours)
print(percent_str)