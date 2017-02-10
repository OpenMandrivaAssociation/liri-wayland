name=$(cat *.spec | grep -i Name: | awk '{print $NF}')
git clone https://github.com/lirios/wayland.git $name
pushd $name
git archive --format=tar --prefix $name-0.9.0.1-$(date +%Y%m%d)/ HEAD | xz -vf > ../$name-0.9.0.1-$(date +%Y%m%d).tar.xz
popd
