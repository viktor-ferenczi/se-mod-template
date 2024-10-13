using VRage.Game.Components;

// ReSharper disable once CheckNamespace
namespace ModTemplate
{
    // ReSharper disable once ClassNeverInstantiated.Global
    [MySessionComponentDescriptor(MyUpdateOrder.NoUpdate)]
    public class ModSessionComponent : MySessionComponentBase
    {
        public static Config Cfg;
        
        public override void LoadData()
        {
            Cfg = new Config();
            base.LoadData();
        }

        protected override void UnloadData()
        {
            base.UnloadData();
            Cfg = null;
        }
    }
}