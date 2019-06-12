# Partial Impl
def build_order(dependencies, non_dependent_projects=None):
	result = []
	if not non_dependent_projects:
		non_dependent_projects = set([dependency[0] for dependency in dependencies]) - set([dependency[1] for dependency in dependencies])
		if not non_dependent_projects:
			return []
	if len(dependencies) == 0:
		result.extend(non_dependent_projects)
		return result
	n_next = []
	for dependency in dependencies:
		if dependency[0] in non_dependent_projects:
			n_next.append(dependency)
	rest = list(set(dependencies) - set(n_next))

	for n in n_next:
		result.append(n[0])
	if n_next:
		non = [n[1] for n in n_next]
		result.extend(build_order(rest, non))
		return result
	else:
		return []

if __name__ == '__main__':
	print('Build Order Impl')
	print(build_order([('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]))
