import click
from spirodraw.drawing_mpl import example_spiro1, spiro_random

# TODO:
# - [ ] maybe add feature to save to svg
# - [ ] chose different color maps
# - [ ] interactively chose the radii
# - [ ] draw hypotroichoids


@click.command()
@click.option('--number', default=3, help="number of hypocycloids")
def main(number):
    """
    Generate @number of hypocycloids with different colors chosen by
    matplotlib with a tendency towards increasing size

    """
    #fig, ax = example_spiro1()
    fig, ax = spiro_random(N=number)
    

    fig.show()


if __name__ == '__main__':
    main()
    
