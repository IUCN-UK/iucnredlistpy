The [International Union for Conservation of
Nature’s](https://www.iucn.org) [Red List of Threatened
Species](https://www.iucnredlist.org) has evolved to become the world’s
most comprehensive information source on the global conservation status
of animal, fungi and plant species. It’s a critical indicator of the
health of the world’s biodiversity.

The [IUCN Red List API](https://api.iucnredlist.org) has been developed
to inform and drive biodiversity conservation and policy change -—
critical steps in protecting essential natural resources. It provides
programmatic access to data including (but limited to); population size,
habitat and ecology, trade and threats to help support informed
conservation decisions.

The iucnredlist R package aims to serve as a client library for the Red
List API, offering the research community and other users an efficient
and user-friendly tool to access and interact with the vital data and
services provided by the IUCN Red List.

We have open sourced this package to promote transparency, enable
research community contributions, and drive adoption of the API. As an
official IUCN-supported library, we shall maintain synchronisation with
any API changes and updates.

## API Usage

The use of the API falls under the same [Terms of
Use](https://www.iucnredlist.org/terms/terms-of-use) as the Red List. By
requesting a token, you are agreeing to abide by the Terms of Use of the
Red List. If your token usage is found to be in breach of our terms of
use, it will be revoked. We kindly request your cooperation in ensuring
responsible and respectful usage of our services.

Please be aware that misusing your API token, such as using it for
information extraction (scraping) rather than making legitimate requests
for non-commercial purposes, may result in your token being rate limited
and/or revoked.

We are committed to maintaining a high-quality service for all users and
have implemented a rate limiting system to ensure our resources are
accessible equally to all. We actively monitor API usage to prevent
abuse. We understand that some users may have unique requirements for
making frequent calls in succession. If you find yourself in such a
situation, we kindly request that you incorporate appropriate delays
between your API calls to ensure smooth operation and prevent
overloading our system, otherwise your token may be further
rate-limited. It’s important to note that the Red List API is primarily
designed to support conservation efforts, particularly in the fields of
education and research. We may need to restrict access if the API is
being used for purposes that do not align with our mission, such as
mobile app development, inclusion in computing courses, or visualization
projects unrelated to conservation.

*Use of the Red List API for commercial purposes is strictly forbidden.
Users who wish to use Red List data for commercial purposes should
consider subscribing to [IBAT](www.ibat-alliance.org).*

### Responsible Usage

We are committed to ensuring fast and reliable access for all users of
this API. To this end, we have implemented rate limiting to maintain
service reliability for all users. Several functions within this package
have an argument called `wait_time` - we recommend setting this to
\>=0.5 seconds (default 0.5 seconds) to avoid rate limiting. If you
build your own functions from this package, we recommend you implement
an appropriate wait time in your code to avoid any such limits.

## Installation

## Example Usage

The `iucnredlistpy` package contains a number of functions to allow quick
access to Red List data. The examples below are some quick-start scripts
to get you familiar with a basic `iucnredlist` workflow.

Before running this code, you must first sign up to the [Red List
API](https://api.iucnredlist.org) to obtain an API token. You can view
(and cycle) your token from your [account
page](https://api.iucnredlist.org/users/edit).

Initialize the client
```
import iucnredlistpy

client = iucnredlistpy.IUCNRedListClient(api_key="your_red_list_api_key")
client.get_biogeographical_realms()
```

## Development

Run tests with 
```
uv run pytest
```

Run the Ruff formatter on all directories and files
```
uv run ruff format
```

Run Ruff check
```
uv run ruff check
```