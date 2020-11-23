# argconfig
argparse + yaml config system

This takes the same format as the argparse.ArgumentParser class; however
it adds the feature of setting a default yaml file for base configuration
to override the default set in the code. Usage has the following overwrite
priority:

command line > config file > default set in code

This enables a flexible configuration based, commandline interface options
at scale.

## Requirements
* Python 3.7+
* pyyaml

## Example
To use the default example (see the source code of argconfig.py)
```
python argconfig.py --foo test --bar 3.0
```
yeilds, by loading the command line settings:
```
foo: test
bar: 3.0
```
While:
```
python argconfig.py
```
yeilds, by loading the example.py config file:
```
foo: test1
bar: 2.0
```