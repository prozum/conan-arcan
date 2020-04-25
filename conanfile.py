import os

from conans import CMake, ConanFile, tools


class ArcanConan(ConanFile):
    name = "arcan"
    version = tools.get_env("GIT_TAG", "0.6.0-pre2")
    description = "Desktop Engine"
    url = "https://gitlab.com/aivero/public/conan/conan-" + name
    license = "LGPL-2.1"
    settings = "os", "arch", "compiler", "build_type"

    def build_requirements(self):
        self.build_requires("cmake/[>=3.15.3]@%s/stable" % self.user)

    def requirements(self):
        self.requires("sdl2/[>=2.0.10]@%s/stable" % self.user)
        self.requires("freetype/[>=2.10.1]@%s/stable" % self.user)
        self.requires("openal/[>=1.20.1]@%s/stable" % self.user)
        self.requires("sqlite/[>=3.30.1]@%s/stable" % self.user)
        self.requires("mesa/[>=19.2.0]@%s/stable" % self.user)
        self.requires("libdrm/[>=2.4.49]@%s/stable" % self.user)
        self.requires("luajit/[>=2.0.5]@%s/stable" % self.user)
        self.requires("libxkbcommon/[>=0.8.4]@%s/stable" % self.user)
        self.requires("libvncserver/[>=0.9.12]@%s/stable" % self.user)

    def source(self):
        tools.get("https://github.com/letoram/arcan/archive/%s.tar.gz" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="%s-%s/src" % (self.name, self.version))
        cmake.build()
        cmake.install()

    def package_info(self):
        self.env_info.XDG_DATA_DIRS.append(os.path.join(self.package_folder, "share"))
