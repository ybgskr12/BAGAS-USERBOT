# MODULES PLUGIN UPDATES

```
`HOW TO ADD MODULES PLUGIN COMMAD`

@register(outgoing=True, pattern='^.hello(?: |$)(.*)')
async def typewriter(typew):
typew.pattern_match.group(1)
await typew.edit("**hello.**")
```
