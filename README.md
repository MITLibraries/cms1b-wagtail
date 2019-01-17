Initial testing of a Wagtail deploy using Zappa (*not* for Production use).

Setup was done following these [instructions](https://gist.github.com/nealtodd/45e230bcfe809d76596a4af3540112d5).

Currently only the dev environment has been created/deployed for testing of Wagtail using Zappa.

Any changes to the environment will require

`zappa update dev`

and potentially:

`zappa manage dev migrate`

and/or:

`zappa manage dev "collectstatic --noinput"`
