"""
HAPT Startup Banner
-------------------
Displays the HAPT welcome banner.
"""

from version import APP_NAME, APP_FULL_NAME, VERSION, AUTHOR


def show_banner():
    """Display the HAPT startup banner."""

    print("=" * 70)
    print(f"{APP_NAME:^70}")
    print(f"{APP_FULL_NAME:^70}")
    print()
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")
    print()
    print("Observe • Analyze • Protect • Execute • Learn")
    print()
    print("Initializing System Engine...")
    print("=" * 70)