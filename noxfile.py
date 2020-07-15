import nox


@nox.session()
def mutation_testing(session):
    session.run('poetry', 'install', external=True)
    session.run('poetry', 'run', 'cosmic-ray', 'init', 'mutation.toml', 'session.sqlite', external=True)
    session.run('poetry', 'run', 'cosmic-ray', 'exec', 'session.sqlite', external=True)
    with open('mutation.html', 'w') as report:
        session.run('poetry', 'run', 'cr-html', 'session.sqlite', external=True, stdout=report)
