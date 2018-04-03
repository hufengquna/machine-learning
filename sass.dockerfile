FROM ml-base

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## source and asset directory
RUN mkdir -p /var/machine-learning/interface/static
RUN mkdir -p /var/machine-learning/src/scss

## copy files into container
COPY src/scss /var/machine-learning/src/scss
COPY hiera /var/machine-learning/hiera
COPY puppet/environment/$ENVIRONMENT/modules/package $ROOT_PUPPET/code/modules/package
COPY puppet/environment/$ENVIRONMENT/modules/compiler $ROOT_PUPPET/code/modules/compiler

##
## manual build workaround
##
## https://github.com/jeff1evesque/machine-learning/issues/2935#issuecomment-378086431
##
RUN npm install -g --unsafe-perm node-sass@4.8.3

## provision with puppet
RUN $PUPPET apply $MODULES/compiler/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
##CMD ["/bin/sh", "-c", "sass"]