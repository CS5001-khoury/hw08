# Homework 08 - Saving State
Programs are about performing tasks. These automated tasks are great, but sometimes you want to return to the 
task while in progress, or save the results of the task. As such, files are ways to hold the "state" of
the information. By reading and writing to files, your program can become more dynamic, remember
content/state between runs, and build upon data. 

For this assignment, we will be returning to a (modified) Star Rating App. Since the last time you worked
on the project, your client had someone else work on redesigning the application. You can see the completed
star rating app by downloading

* [star_rating_app.py](star_rating_app.py)
* [star_rating_utils.py](star_rating_utils.py)
* [star_rating_loader.py](star_rating_loader.py)

Applications are often designed across multiple files to help you isolate the work you are doing. The main 
app is star_rating_app, but utils are a number of functions that can help with the applications. They are
also generalized enough they can help in other ways throughout the application. Loader will be the fill you are
working on, and that is saving and loading data back into the application. 

## Reviewing the Provided Code
👉🏽 **TASK**: Review and reflect upon the provided code

Take time to review the provided code. In your README.md, add a section that talks about the design. What are
some things you observe about the design of the "new" star rating. Comment both on the big level (the entire program)
and the little level (a single function or two). At the little level, how does a function differ from your implementation?
While you are open on what to talk about, a common conversation would be the use (or lack of use) of globals, default
parameters, and use of lines. For the most part, while there are some more ways to handle the problem, the code
was specifically written using only features we have covered with the addition of separating the files out to their
various components. 

## Write save_movies(filename, movies)
👉🏽 **TASK**: Write save_movies, and associated tests

In star_app_loader, find the save_movies function. Your goal is to write to the filename provided
every movie + rating, separated by commas. For example, if your movies list looked like the following

```python 
movies = [
   ("Princess Brice", 5.0),
   ("V", 5.0),
   ("Jurassic Shark", 1.0),
   ("Honey, I shrunk the kids!", 2.0)
    ]
```

The file you would write out to, would have the contents
```text
Princess Brice,5.0
V,5.0
Jurassic Shark,1.0
Honey, I shrunk the kids!,2.0
```

### Testing
Testing files can be difficult. Often the best way to do it, is to generate/write by hand a 'correct' file given a 
provided input. Then use that input to see if the same file gets generated.  Comparing files is so common, there is the
`diff` command in windows, linux, mac that you can compare two files.  

For example, I could save the above content to something like  `test1_correct.txt`, and then when I run my program,
I would call:

```python
from star_rating_loader import save_movies

def test1():
    movies = [
       ("Princess Brice", 5.0),
       ("V", 5.0),
       ("Jurassic Shark", 1.0),
       ("Honey, I shrunk the kids!", 2.0)
    ]
    save_movies("test1.txt", movies) # correct version in test1_correct.txt
```

A more elegant solution would be to read back in the file just saved as a simple read, and compare contents. For example

```python
def compare_files(filename1, filename2):
   with open(filename1) as file1, open(filename2) as file2:
      contents_one = file1.read()
      contents_two = file2.read()
      if contents_one != contents_two:
         print("failed test!")
         return True
   return False

def main():
   counter = 0
   test1()
   if compare_files("test1.txt", "test1_correct.txt"):
    counter += 1
    print(f"Failed: {counter} tests.")
```


👉🏽 **TASK**:  Add tests. You should have a few tests for the save function 
(in a separate file called `test_star_rating_loader.py`). You will submit your correct.txt files with
your tests, so we know you did a comparison. 

👉🏽 **TASK**: Run star_rating_app.py. If you did it correctly, it should be saving to movie_ratings.txt the
various movies you are entering. 

## Movie Loader

Now that you have completed the writer, run the program and make sure to save out a few movies. Your next task
is to write the movie loader `load_movies(filename)`

`load_movies` takes in a filename, and adds movies and ratings as tuples to a list. It then returns that list. 
A few other conditions
* If the line is invalid/has a ValueError, `"Error reading line: {line}"` to `stderr`, where the line is the line
in the file in question, and then skip it / keep reading lines. 
* You may want to look at the utility functions in star_rating_utils.

For example, if a file has the following contents:
```text
Princess Brice,5
V,5.0
V2,five
Jurassic Shark,1.0
Honey, I shrunk the kids!,2
```
It will create the following list:

```python
movies = [
       ("Princess Brice", 5.0),
       ("V", 5.0),
       ("Jurassic Shark", 1.0),
       ("Honey, I shrunk the kids!", 2.0)
    ]
```
while also printing to `stderr`, "Error reading line: V2,five".

### Add Tests
Similar to writing a file, make sure you add tests to reading a file. This is a bit easier, as you can read the file
and make sure the list generated is correct. 

## README.md
As with your other assignments, include the readme. Make sure to answer the questions above about design. 

Additionally, reflect on what features would you like to add to the application? Does it make sense to only 
have a fixed file? Also think about other areas in your life that can benefit from an application. What are
some of those areas, and what would an application involve?



## 📝 Grading Rubric

Make sure to submit, even if you didn't modify/edit
* star_rating_loader.py
* test_star_rating_loader.py
* star_rating_utils.py (you shouldn't have modified this)
* star_rating_app.py (you shouldn't have modified this)
* README.md


1. Learning (AG)
   * Able to save movies list to file
2. Approaching  (AG)
   * Able to load simple file into movies list
3. Meets  (AG)
   * Able to load file with errors lines into movies list
   * Handles edge cases for saving
   * Passes code style checks
4. Exceeds  (MG)
   * Design questions answered in readme
   * Proper use of docstrings/comments/design
   * Reflection questions answered in readme
   * Other application discussions in readme file
   * Student has provided tests for loader and save, along with files
     used in testing. 


AG - Auto-graded  
MG - Manually graded


## 📚 Additional Resources
* [Real Python Read/Write Files](https://realpython.com/read-write-files-python/)
* [Free Code Camp Reading Pythong Files](https://www.freecodecamp.org/news/how-to-read-files-in-python/)
* [Using with to read/write files](https://www.statology.org/with-open-python/)