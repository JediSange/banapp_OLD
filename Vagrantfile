VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "nishoba"
  config.vm.network :forwarded_port, host: 8000, guest: 8000
  config.vm.provision :shell, path: "config/vagrant_root.sh"
  config.vm.provision :shell, path: "config/vagrant_user.sh", privileged: false
  config.ssh.forward_agent = true
end
