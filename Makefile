.PHONY: help
help:
	@echo "available targets -->\n"
	@cat Makefile | grep ".PHONY" | grep -v ".PHONY: _" | sed 's/.PHONY: //g'



.PHONY: build
build:
	podman build -f ./Containerfile -t docker.io/lynnsanity/pcl:$$(cat VERSION)

.PHONY: release
release:
	podman build -f ./Containerfile -t docker.io/lynnsanity/pcl:$$(cat VERSION)
	podman push docker.io/lynnsanity/pcl:$$(cat VERSION)
