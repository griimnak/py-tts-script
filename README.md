<h1>
    Python TTS Script
</h1>

This is a simple TTS script that can be imported and used as a module or used via command line.

Should work on MacOS aswell, not tested though.
###### `speak_linux()` depends on the `say` package which is available via apt or brew

### Usage
```sh
python speak.py "Hello world"
```

### Or as a module:
```python
import speak

speak.speak_windows("Hello world")
# speak.speak_linux("Hello world")
```
