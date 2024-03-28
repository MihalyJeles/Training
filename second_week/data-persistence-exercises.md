1. Use the below list to write all names to a file where each name is on a new line.

    ```py
    people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
    ```

1. Extend this to use `try-catch`.
1. Extend this to use `try-catch-finally` and close the file.
1. Extend this to make use of the file context manager (hint: use the keyword `with`).
1. Create a text file with repeated names such as:

```sh
John
James
John
Sally
John
Sally
Mark
John
```

Create a Python file that reads the file in. Create a dictionary where the keys are the names from the file and the values are the number of times each name appears in the text file.

Write out to another file where each line looks like:

```sh
Name: John, Count: 4
```
