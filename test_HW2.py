import visutils

g, gr = visutils.load_and_prepare_cmd('fieldA.csv')
visutils.interactive_hess(g, gr)
