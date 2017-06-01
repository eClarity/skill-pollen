# Allergy Tracker Skill for Mycroft

Based off of another allergy scraper that no longer works.

This is a skill to add https://weather.com/ allergy tracker support to
[Mycroft](https://mycroft.ai). Currently you can ask for breathing comfort level and allergen levels

## Installation

Clone the repository into your `~/.mycroft/skills` directory. Then install the
dependencies inside your mycroft virtual environment:

If on picroft just skip the workon part and the directory will be /opt/mycroft/skills

```
cd ~/.mycroft/skills
https://github.com/eClarity/skill-pollen
workon mycroft
cd PollenSkill
pip install -r requirements.txt
```



## Configuration

Add a block to your `~/.mycroft/mycroft.conf` file like this:

```
  "PollenSkill": {
    "zipcode": yourziphere
  }
```


