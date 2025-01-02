---
created: 2024-07-28T12:00:00
modified: 2024-12-28T11:09:23
created-link: "[[20240728]]"
document: 
status: tool/star
tags: browser 
type: tool
---

## Profile

```
.
├── AlternateServices.txt
├── ClientAuthRememberList.txt
├── SecurityPreloadState.txt
├── SiteSecurityServiceState.txt
├── Telemetry.FailedProfileLocks.txt
├── addonStartup.json.lz4
├── addons.json
├── autofill-profiles.json
├── blocklist.xml
├── bookmarkbackups # This folder stores bookmark backup files,
|                   # which can be used to restore your bookmarks.
├── broadcast-listeners.json
├── browser-extension-data
├── cert9.db        # all your security certificate settings and
|                   # any SSL certificates you have imported into
|                   # Firefox.
├── cert_override.txt
├── compatibility.ini
├── containers.json # the details of containers used by the Container
|                   # Tabs feature, including those created by extensions
|                   # such as Facebook Container.
├── content-prefs.sqlite # Site-specific preferences:
├── cookies.sqlite       # a bit of information stored on your computer
|                        # by a website you’ve visited
├── crashes
├── datareporting
├── enumerate_devices.txt
├── extension-preferences.json
├── extension-settings.json
├── extensions           # stores files for any extensions you have installed
├── extensions.json
├── favicons.sqlite      # all of the favicons for your Firefox bookmarks.
├── features
├── formhistory.sqlite   # This file remembers what you have searched
|                        # for in the Firefox search bar and what
|                        # information you’ve entered into forms on websites.
├── gmp
├── gmp-gmpopenh264
├── gmp-widevinecdm
├── handlers.json        # preferences that tell Firefox what to do when
|                        # it comes across a particular type of file.
├── key4.db              # Passwords
├── logins-backup.json
├── logins.json          # Passwords
├── mediacapabilities
├── memory-report.json.gz
├── minidumps
├── notificationstore.json
├── parent.lock
├── permissions.sqlite   # Site-specific preferences
├── pkcs11.txt           # security module configuration.
├── places.sqlite        # This file contains all your Firefox bookmarks
|                        # and lists of all the files you've downloaded
|                        # and websites you’ve visited.
├── pluginreg.dat
├── prefs.js             # customized user preference settings, such as
|                        # changes you make in Firefox Settings dialogs.
|                        # The optional user.js file, if one exists,
|                        # will override any modified preferences.
├── protections.sqlite
├── saved-telemetry-pings
├── search.json.mozlz4   # This file stores user-installed search engines
├── security_state
├── serviceworker.txt
├── sessionCheckpoints.json
├── sessionstore-backups
├── sessionstore.jsonlz4  # the currently open tabs and windows
├── shader-cache
├── shield-preference-experiments.json
├── signedInUser.json
├── storage
├── storage-sync-v2.sqlite
├── storage-sync-v2.sqlite-shm
├── storage-sync-v2.sqlite-wal
├── storage-sync.sqlite
├── storage.sqlite
├── times.json
├── weave
├── webappsstore.sqlite   # DOM storage,  provide a larger, more secure,
|                         # and easier-to-use alternative to storing
|                         # information in cookies.
└── xulstore.json         # toolbar and window size/position settings
```

### Windows

default location is `%APPDATA%\Mozilla\Firefox\Profiles\`[^windows-profile]

## Custom Config
### [[windows]]

#### Limit memory using

```yaml
browser.cache.memory.capacity: 8192000
```

#### History max to be keep

https://superuser.com/questions/1269516/what-exactly-does-the-number-listed-under-places-history-expiration-transient-c

```yaml
places.history.expiration.transient_current_max_pages
# https://support.mozilla.org/en-US/questions/1039372

browser.migrate.chrome.history.limit
browser.migrate.chrome.history.maxAgeInDays
# https://superuser.com/questions/1635171/firefox-doesnt-import-all-history-from-chrome

places.history.expiration.max_pages
# https://www.reddit.com/r/firefox/comments/u417w8/how_long_does_firefox_keep_history_for/
```

### User Agent (UA)

Go `about:config` to create a String named ` general.useragent.override` [^create-custom-ua]

Value could be an iPad:

```
Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10
```

Or an iPhone:

```
Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1
```

Or a Mac:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15
```

Check your current on https://www.whatsmyua.info/

More UA check via: https://www.whatismybrowser.com/guides/the-latest-user-agent/ios

### [[ios]]

[^windows-profile]: via: [MZHistoryView: View the list of visited web sites in Firefox / Mozilla browsers](http://www.nirsoft.net/utils/mozilla_history_view.html) & https://support.mozilla.org/bm/questions/754699
[^create-custom-ua]: [Is there any way to change user agent string on Firefox 80.1.3 for Android? : r/firefox](https://www.reddit.com/r/firefox/comments/it7jqx/is_there_any_way_to_change_user_agent_string_on/)
