# Section 16: Unpacking Operators (* and **)

* **Sequence Unpacking (`*`):**
  * Number of target variables must match sequence length unless using `*rest`.
  * `first, *remaining, last = iterable`: Captures unspecified middle elements into a `list`.
* **Argument Unpacking:**
  * `*list_or_tuple`: Expands elements into separate positional arguments for a function call.
  * `**dict`: Expands key-value pairs into named keyword arguments matching parameter names.
* **Dictionary Merging (`**`):**
  * `{**dict_a, **dict_b}` creates a new merged dictionary.
  * If duplicate keys exist, values from the rightmost dictionary overwrite earlier ones.