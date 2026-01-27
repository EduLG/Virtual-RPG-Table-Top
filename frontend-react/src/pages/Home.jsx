import React from "react";
import { Button } from "@radix-ui/themes";

const Home = () => {
  return (
    <div className="flex min-h-screen">
      <aside className="w-1/5 bg-gray-800 text-white p-4">
        <nav className="space-y-4">
          <h2 className="text-xl font-bold">Navbar</h2>
          <div className="flex flex-col gap-2">
            <Button className="w-full px-4 py-2 text-left rounded hover:bg-gray-700">
              Team
            </Button>
            <Button className="w-full px-4 py-2 text-left rounded hover:bg-gray-700">
              Equipment
            </Button>
            <Button className="w-full px-4 py-2 text-left rounded hover:bg-gray-700">
              Dungeons
            </Button>
          </div>
        </nav>
      </aside>

      <main className="w-4/5 p-6 bg-gray-100">
        <div className="grid grid-cols-2 grid-rows-2 gap-6 h-full">
          {[1, 2, 3, 4].map((card) => (
            <div
              key={card}
              className="bg-white rounded-xl shadow font-semibold"
            >
              <div className="grid grid-cols-2">
                <div>01</div>
                <div>02</div>
                <div className="col-span-2 w-full">03</div>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
};

export default Home;
