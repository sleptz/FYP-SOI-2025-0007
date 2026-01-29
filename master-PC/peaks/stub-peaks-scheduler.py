import time

pods = ["pod1", "pod2", "pod3"]
nodes = ["node1", "node2"]

print("Stub PEAKS scheduler started (offline demo)")

for iteration in range(3):
	for i, pod in enumerate(pods):
		node = nodes[i % len(nodes)]
		print(f"Scheduling {pod} to {node} (offline demo)")
	time.sleep(5)

print("Stub PEAKS scheduler finished")
