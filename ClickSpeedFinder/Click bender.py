from tkinter import *
import time
import json

time_dict = {}
clicks = 0


def count_click(event):
    global clicks, time_dict
    clicks += 1
    time_dict[time.ctime(time.time()).split()[3]] = [clicks, time.perf_counter()]
    # print(time.process_time(), time.perf_counter())


root = Tk()
root.geometry('500x500+0+0')
root.title('Click bender')
l = Label(root, text='Click here !', height=10, width=24, bd=1)
l.pack()
l.bind('<ButtonPress-1>', count_click)
l.bind('<ButtonPress-3>', count_click)
root.mainloop()


root2 = Tk()
text = Text(root2)
text.pack(expand=True, fill=BOTH)
avg_clicks = []
for i in range(len(time_dict.keys())):
    avg_clicks.append(int(time_dict[list(time_dict.keys())[i]][0]) - int(time_dict[list(time_dict.keys())[i-1]][0]))
    text.insert(END, f"{list(time_dict.keys())[i]} : {time_dict[list(time_dict.keys())[i]][0]} \t\t {time_dict[list(time_dict.keys())[i]][1]}"
                     f"\t\t{int(time_dict[list(time_dict.keys())[i]][0]) - int(time_dict[list(time_dict.keys())[i-1]][0])}\n")

text.replace(text.search('-', '1.0', stopindex='1.0 lineend'), '1.0 lineend', f"{time_dict[list(time_dict.keys())[0]][0]}")
avg_clicks[0] = int(time_dict[list(time_dict.keys())[0]][0])
text.insert(END, f"\n\n Average Clicks: {sum(avg_clicks)/len(avg_clicks)} --> {round(sum(avg_clicks)/len(avg_clicks))}")
root2.mainloop()

with open('avg_click_log.json', 'r') as file1:
    click_dict = dict(json.load(file1))

click_dict[f"{time.ctime(time.time())}"] = {
    "Time_Period": f"{list(time_dict.keys())[0]}-->{list(time_dict.keys())[-1]}", "Total_Clicks": clicks,
    "Avg_Clicks": f"{sum(avg_clicks)/len(avg_clicks)}-->{round(sum(avg_clicks)/len(avg_clicks))}"
    }
print(f"Log saved at: {time.ctime(time.time())}")
json_object = json.dumps(click_dict, indent=4)
with open('avg_click_log.json', 'w') as file2:
    file2.write(json_object)
