# emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the NiBabel package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
# General Gifti Input - Output to and from the filesystem
# Stephan Gerhard, Oktober 2010
##############

import os

from . import parse_gifti_fast as gfp
reload(gfp)

def read(filename):
    """ Load a Gifti image from a file
    
    Parameters
    ----------
    filename : string
        The Gifti file to open, it has usually ending .gii
        
    Returns
    -------
    img : GiftiImage
        Returns a GiftiImage
        
     """
    if not os.path.isfile(filename):
        raise IOError("No such file or directory: '%s'" % filename)
    return gfp.parse_gifti_file(filename)


def write(image, filename):
    """ Save the current image to a new file

    Parameters
    ----------
    image : GiftiImage
        A GiftiImage instance to store 
    filename : string
        Filename to store the Gifti file to

    Returns
    -------
    None
    
    Notes
    -----
    The Gifti spec suggests using the following suffixes to your
    filename when saving each specific type of data:

    .gii
        Generic GIFTI File
    .coord.gii
        Coordinates
    .func.gii
        Functional
    .label.gii
        Labels
    .rgba.gii
        RGB or RGBA
    .shape.gii
        Shape
    .surf.gii
        Surface
    .tensor.gii
        Tensors
    .time.gii
        Time Series
    .topo.gii
        Topology
    """

    f = open(filename, 'w')
    f.write(image.to_xml())
    f.close()

    
