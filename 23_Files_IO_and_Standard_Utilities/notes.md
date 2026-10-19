# Section 23: Files I/O, Compression, Dates & Security Utilities

* **File Operations & Pathlib:**
  * Use `pathlib.Path` for cross-platform filesystem navigation over raw string paths.
  * Always access file streams with `with open(..., mode, encoding="utf-8") as f:` to guarantee safe handle closure.
  * Remove files using `path.unlink()` and directories using `path.rmdir()`.

* **CSV & Zip Handling:**
  * `csv.reader` and `csv.writer` handle parsing and escaping row-based data correctly.
  * `zipfile.ZipFile(filename, mode)` reads and generates compressed `.zip` archives.

* **Dates and Times (`datetime` & `time`):**
  * **`strftime` (String Format Time):** Converts datetime objects into formatted strings.
  * **`strptime` (String Parse Time):** Parses formatted date strings into datetime objects.
  * **`timedelta`:** Computes differences and offsets across dates and times.
  * **`time.time()` & `time.sleep()`:** Used for benchmarking elapsed intervals and throttling execution.

* **Randomness vs Security:**
  * **`random` module:** Pseudo-random numbers suitable for data shuffling, simulations, and non-sensitive logic.
  * **`secrets` module:** Cryptographically strong pseudo-random number generator (CSPRNG) required for password generation, API keys, CSRF protection, and OTP tokens.