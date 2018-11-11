class Deployment
  def initialize(args)
    @instances_tag = args[:instances_tag]
    @profile = args[:profile]
    @key_path = args[:key_path]
    @region = args[:region]
  end

  def deploy
    script_path = './scripts/fetch_instances.sh'
    system("
      #{script_path} #{@instances_tag} #{@key_path} #{@region} #{@profile}
    ")
  end
end