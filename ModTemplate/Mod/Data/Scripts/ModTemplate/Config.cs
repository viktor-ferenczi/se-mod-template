// ReSharper disable once CheckNamespace

using System;
using System.Collections.Generic;
using Sandbox.ModAPI;
using VRage.Utils;

// ReSharper disable once CheckNamespace
namespace ModTemplate
{
    public class Config: BaseConfig
    {
        private const string ConfigFileName = "ModTemplate.ini";
        private static readonly Type ModType = typeof(Config);

        public Config()
        {
            MyLog.Default.WriteLineAndConsole($"ModTemplate: Configuration file in the world's Storage folder: {ConfigFileName}");

            string text = null;
            if (MyAPIGateway.Utilities.FileExistsInWorldStorage(ConfigFileName, ModType))
            {
                using (var f = MyAPIGateway.Utilities.ReadFileInWorldStorage(ConfigFileName, ModType))
                {
                    text = f.ReadToEnd();
                }
            }
            
            var errors = new List<string>();
            if (string.IsNullOrEmpty(text) || TryParse(text, Defaults, errors))
            {
                using (var f = MyAPIGateway.Utilities.WriteFileInWorldStorage(ConfigFileName, ModType))
                {
                    text = FormatIni();
                    f.Write(text);
                }
            }
            else
            {
                MyLog.Default.WriteLineAndConsole("ModTemplate: Failed to parse configuration file");
                foreach (var error in errors)
                {
                    MyLog.Default.WriteLineAndConsole($"ModTemplate: {error}");
                }
                MyLog.Default.WriteLineAndConsole("ModTemplate: Starting with default configuration");
            }
        }

        protected override void AddOptions()
        {
            // TODO: Add your options. Supported types: bool, int, float, double, string
            Comments["MyOption"] = "Describe the config option here";
            Defaults["MyOption"] = 42;
            
            // ...
        }

        // TODO: Add accessors to your options
        public float MyOption => (float)this["MyOption"];
        // ...
    }
}