require 'spec_helper'

describe file('/etc/ansible/facts.d') do
  it { should exist }
  it { should be_directory }
  it { should be_mode '755' }
  it { should be_owned_by 'root' }
  it { should be_grouped_into 'root' }
end

describe file('/etc/ansible/facts.d/foo.fact') do
  it { should exist }
  it { should be_file }
  it { should be_mode '755' }
  it { should be_owned_by 'root' }
  it { should be_grouped_into 'root' }
end
