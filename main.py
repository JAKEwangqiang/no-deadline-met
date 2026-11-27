#!/usr/bin/env python3
"""One Line, No Deadline Met — entry.

The line is the entry's title on make.fun (one line, at most 200 characters).
Running this prints it.
"""
LINE = "I moved the deadline to next week — it declined the calendar invite."

def excuse():
    """Return the missed-deadline excuse."""
    return LINE

def main():
    print(excuse())

if __name__ == "__main__":
    main()
