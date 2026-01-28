import React from "react";
import { Button } from "@radix-ui/themes";
import adventurer from "../assets/resources/character-templates/adventurer.png";

const Home = () => {
  return (
    <div className="flex min-h-screen bg-[#2b1e14]">
      <aside className="w-1/5 bg-[#3b2a1a] text-[#f5e6c8] p-4 border-r border-[#6b4f2a]">
        <nav className="space-y-4">
          <h2 className="text-xl font-bold">Navbar</h2>
          <div className="flex flex-col gap-2">
            <Button className="w-full px-4 py-2 text-left rounded bg-[#4a3420] text-[#f5e6c8] hover:bg-[#6b4f2a]">
              Team
            </Button>
            <Button className="w-full px-4 py-2 text-left rounded bg-[#4a3420] text-[#f5e6c8] hover:bg-[#6b4f2a]">
              Equipment
            </Button>
            <Button className="w-full px-4 py-2 text-left rounded bg-[#4a3420] text-[#f5e6c8] hover:bg-[#6b4f2a]">
              Dungeons
            </Button>
          </div>
        </nav>
      </aside>

      <main className="w-4/5 p-6 bg-[#2b1e14] h-screen">
        <div className="grid grid-cols-2 grid-rows-2 gap-6 h-full">
          {[1, 2, 3, 4].map((card) => (
            <div
              key={card}
              className="bg-[#f3e5c8] rounded-xl shadow-lg border border-[#b08d57] text-[#3b2a1a]"
            >
              <div className="grid grid-cols-2 grid-rows-2 h-full">
                <div className="p-3 flex items-center justify-center bg-[#e6d3a3] rounded-tl-xl">
                  <img
                    src={adventurer}
                    alt="Adventurer"
                    className="w-full h-full object-contain"
                  />
                </div>

                <div className="flex items-center justify-center font-semibold">
                  02
                </div>

                <div className="col-span-2 flex items-center justify-center bg-[#c4a66a] rounded-b-xl">
                  03
                </div>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
};

export default Home;
